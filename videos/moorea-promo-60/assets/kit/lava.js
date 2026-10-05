/* ==========================================================================
   MOOREA LAVA ENGINE — deterministic, seek-safe WebGL lava sea + 2D embers.
   The look is lifted from the app's Plan screen (black basalt plates, orange
   to yellow molten veins) and its ember particles.

   USAGE (inside a frame, synchronously while building the timeline):
     var lava = MooreaLava.create(canvasEl, { seed: 3 });           // WebGL
     var embers = MooreaEmbers.create(canvas2dEl, { seed: 7, count: 70 });
     var P = { t: 0, heat: 1, zoom: 1, panX: 0, panY: 0, tilt: 0.6,
               coolX: 0.5, coolY: 0.5, coolR: 0, eruptX: 0.5, eruptY: 0.5, erupt: 0 };
     function draw() { lava.render(P); embers.render(P.t, { boost: 1 }); }
     tl.to(P, { t: DURATION, duration: DURATION, ease: 'none', onUpdate: draw }, 0);
     tl.to(P, { coolR: 1.6, duration: 0.6, ease: 'power2.out', onUpdate: draw }, 2.0);
     draw();
   Every visual is a pure function of P — no clocks, no randomness at render.

   PARAMETERS (all optional, defaults shown):
     t      time in seconds (drives the flow)              0
     heat   0 = cold dark basalt, 1 = normal, 2 = blazing  1
     zoom   >1 zooms in                                    1
     panX/panY  camera travel over the lava (world units)  0
     tilt   0 = top-down, 1 = low grazing horizon view     0
     horizon  screen y (0 top..1 bottom) of the horizon when tilt>0   0.30
     coolX/coolY/coolR  a quench ring centred at (x,y) in screen 0..1;
            inside the radius the lava turns into the app's navy basalt
            with a bright steam line at the edge            r=0 (off)
     erupt/eruptX/eruptY  white-hot blast at a point (0..1 amount) 0
     flash  0..1 adds a global white-orange overexposure   0
   ========================================================================== */
(function () {
  var VERT = 'attribute vec2 p; void main(){ gl_Position = vec4(p, 0.0, 1.0); }';
  var FRAG = [
    'precision highp float;',
    'uniform vec2 res; uniform float t, heat, zoom, tilt, horizon, coolR, erupt, flash, seed;',
    'uniform vec2 pan, cool, eruptP;',
    'float h21(vec2 p){ p = fract(p*vec2(123.34, 456.21)+seed*0.137); p += dot(p, p+45.32); return fract(p.x*p.y); }',
    'vec2 h22(vec2 p){ float n = h21(p); return vec2(n, h21(p+n+17.0)); }',
    'float noise(vec2 p){ vec2 i=floor(p), f=fract(p); vec2 u=f*f*(3.0-2.0*f);',
    '  return mix(mix(h21(i),h21(i+vec2(1,0)),u.x), mix(h21(i+vec2(0,1)),h21(i+vec2(1,1)),u.x), u.y); }',
    'float fbm(vec2 p){ float v=0.0, a=0.5; for(int i=0;i<5;i++){ v+=a*noise(p); p=p*2.03+vec2(1.7,9.2); a*=0.5; } return v; }',
    /* voronoi: distance to nearest cell border (F2-F1) -> basalt plate cracks */
    'vec3 voro(vec2 p){ vec2 n=floor(p), f=fract(p); float d1=8.0, d2=8.0; vec2 id=vec2(0.0);',
    '  for(int j=-1;j<=1;j++) for(int i=-1;i<=1;i++){ vec2 g=vec2(float(i),float(j)); vec2 o=h22(n+g);',
    '    o = 0.5+0.42*sin(t*0.35 + 6.2831*o); vec2 r=g+o-f; float d=dot(r,r);',
    '    if(d<d1){ d2=d1; d1=d; id=n+g; } else if(d<d2){ d2=d; } }',
    '  return vec3(sqrt(d2)-sqrt(d1), h21(id), 0.0); }',
    'vec3 molten(float k){ k=clamp(k,0.0,1.6);',
    '  vec3 c = mix(vec3(0.30,0.02,0.0), vec3(0.88,0.20,0.03), smoothstep(0.0,0.45,k));',
    '  c = mix(c, vec3(1.0,0.56,0.10), smoothstep(0.40,0.85,k));',
    '  c = mix(c, vec3(1.0,0.86,0.42), smoothstep(0.80,1.15,k));',
    '  c = mix(c, vec3(1.0,0.97,0.86), smoothstep(1.10,1.55,k)); return c; }',
    'void main(){',
    '  vec2 uv = gl_FragCoord.xy/res; uv.y = 1.0-uv.y;',            /* 0,0 = top-left like CSS */
    '  float asp = res.x/res.y;',
    '  vec2 sp = vec2((uv.x-0.5)*asp, uv.y-0.5);',
    '  vec2 w; float fog = 0.0; float sky = 0.0;',
    '  if (tilt > 0.001) {',
    '    float hz = horizon; float yy = uv.y - hz;',
    '    if (yy <= 0.002) { sky = 1.0; yy = 0.002; }',
    '    float depth = mix(1.0, 0.16/(yy+0.02), tilt);',
    '    w = vec2(sp.x*depth, depth*1.4 + (1.0-tilt)*sp.y);',
    '    fog = tilt*smoothstep(2.5, 9.0, depth);',
    '  } else { w = sp; }',
    '  w = w/zoom*3.2 + pan;',
    /* domain warp for flowing magma */
    '  vec2 q = vec2(fbm(w*0.9 + vec2(0.0, t*0.12)), fbm(w*0.9 + vec2(5.2, -t*0.10)));',
    '  vec2 ww = w + 0.55*q;',
    '  vec3 v = voro(ww*1.15);',
    '  float crack = 1.0 - smoothstep(0.0, 0.11 + 0.05*fbm(ww*3.0), v.x);',
    '  float flow = fbm(ww*2.2 + vec2(t*0.25, t*0.18));',
    '  float pulse = 0.85 + 0.15*sin(t*2.1 + v.y*6.28);',
    '  float k = crack*(0.75 + 0.6*flow)*pulse;',
    '  k += smoothstep(0.62, 0.95, flow)*0.35*(1.0-crack);',     /* molten pools inside plates */
    '  k *= heat;',
    '  float plate = 0.055 + 0.05*fbm(ww*5.0) + 0.03*v.y;',
    '  vec3 basalt = vec3(plate*0.95, plate*0.92, plate*0.98);',
    '  vec3 col = mix(basalt, molten(k), smoothstep(0.08, 0.35, k));',
    '  col += molten(k)*0.25*smoothstep(0.2,1.0,k);',              /* bloom-ish */
    /* quench ring: navy basalt inside, steam line at the edge */
    '  if (coolR > 0.0) { vec2 cd = vec2((uv.x-cool.x)*asp, uv.y-cool.y); float d = length(cd);',
    '    float inside = 1.0 - smoothstep(coolR-0.02, coolR+0.02, d);',
    '    vec3 navy = mix(vec3(0.059,0.090,0.133), vec3(0.078,0.125,0.188), fbm(ww*4.0));',
    '    navy += vec3(0.88,0.33,0.07)*crack*0.22*(1.0-smoothstep(0.0, 0.5, coolR-d));',
    '    col = mix(col, navy, inside);',
    '    float edge = exp(-pow((d-coolR)*70.0, 2.0)); col += vec3(1.0,0.52,0.18)*edge*0.42; }',
    '  if (erupt > 0.0) { vec2 ed = vec2((uv.x-eruptP.x)*asp, uv.y-eruptP.y); float e = exp(-dot(ed,ed)*18.0/(0.2+erupt));',
    '    col += molten(1.4)*e*erupt*1.4; }',
    '  if (sky > 0.5) { float g = exp(-(horizon-uv.y)*7.0); col = mix(vec3(0.035,0.04,0.06), vec3(0.55,0.14,0.03), g*0.9*heat); }',
    '  col = mix(col, vec3(0.30,0.08,0.02)*heat + vec3(0.03), fog*0.85);',
    '  vec2 vg = uv-0.5; col *= 1.0 - dot(vg,vg)*0.9;',
    '  col = mix(col, vec3(1.0,0.86,0.62), flash);',
    '  gl_FragColor = vec4(col, 1.0);',
    '}'
  ].join('\n');

  function compile(gl, type, src) {
    var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error('lava shader: ' + gl.getShaderInfoLog(s));
    return s;
  }

  function create(canvas, opts) {
    opts = opts || {};
    var gl = canvas.getContext('webgl', { preserveDrawingBuffer: true, antialias: false, premultipliedAlpha: false })
          || canvas.getContext('experimental-webgl', { preserveDrawingBuffer: true });
    if (!gl) { return { render: function () {} }; }
    var pr = gl.createProgram();
    gl.attachShader(pr, compile(gl, gl.VERTEX_SHADER, VERT));
    gl.attachShader(pr, compile(gl, gl.FRAGMENT_SHADER, FRAG));
    gl.linkProgram(pr); gl.useProgram(pr);
    var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    var loc = gl.getAttribLocation(pr, 'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
    var U = {}; ['res', 't', 'heat', 'zoom', 'tilt', 'horizon', 'coolR', 'erupt', 'flash', 'seed', 'pan', 'cool', 'eruptP']
      .forEach(function (n) { U[n] = gl.getUniformLocation(pr, n); });
    var seed = opts.seed || 1;
    function v(p, k, d) { return (p && typeof p[k] === 'number') ? p[k] : d; }
    function render(p) {
      gl.viewport(0, 0, canvas.width, canvas.height);
      gl.uniform2f(U.res, canvas.width, canvas.height);
      gl.uniform1f(U.t, v(p, 't', 0)); gl.uniform1f(U.heat, v(p, 'heat', 1)); gl.uniform1f(U.zoom, v(p, 'zoom', 1));
      gl.uniform1f(U.tilt, v(p, 'tilt', 0)); gl.uniform1f(U.horizon, v(p, 'horizon', 0.3));
      gl.uniform1f(U.coolR, v(p, 'coolR', 0)); gl.uniform1f(U.erupt, v(p, 'erupt', 0)); gl.uniform1f(U.flash, v(p, 'flash', 0));
      gl.uniform1f(U.seed, seed);
      gl.uniform2f(U.pan, v(p, 'panX', 0), v(p, 'panY', 0));
      gl.uniform2f(U.cool, v(p, 'coolX', 0.5), v(p, 'coolY', 0.5));
      gl.uniform2f(U.eruptP, v(p, 'eruptX', 0.5), v(p, 'eruptY', 0.5));
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }
    return { render: render, gl: gl };
  }

  /* ---------------- embers: seeded, deterministic ---------------- */
  function mulberry(a) { return function () { a |= 0; a = a + 0x6D2B79F5 | 0; var t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function createEmbers(canvas, opts) {
    opts = opts || {};
    var ctx = canvas.getContext('2d');
    var rnd = mulberry(opts.seed || 7), n = opts.count || 60, P = [];
    for (var i = 0; i < n; i++) P.push({ x: rnd(), y: rnd(), sp: 0.05 + rnd() * 0.16, sw: rnd() * 6.28, sa: 0.01 + rnd() * 0.03,
      r: 1.5 + rnd() * rnd() * 7, ph: rnd() * 6.28, fl: 3 + rnd() * 9 });
    function render(t, o) {
      o = o || {}; var boost = o.boost == null ? 1 : o.boost, rise = o.rise == null ? 1 : o.rise, W = canvas.width, H = canvas.height;
      ctx.clearRect(0, 0, W, H); ctx.globalCompositeOperation = 'lighter';
      for (var i = 0; i < n; i++) {
        var p = P[i], y = ((p.y - t * p.sp * rise) % 1 + 1) % 1, x = p.x + Math.sin(t * 0.8 + p.sw) * p.sa;
        var a = (0.55 + 0.45 * Math.sin(t * p.fl + p.ph)) * Math.min(1, y * 4) * boost; if (a <= 0.01) continue;
        var px = x * W, py = y * H, r = p.r * (W / 1920) * (o.scale || 1);
        var g = ctx.createRadialGradient(px, py, 0, px, py, r * 4);
        g.addColorStop(0, 'rgba(255,240,190,' + a + ')'); g.addColorStop(0.18, 'rgba(255,207,45,' + a * 0.9 + ')');
        g.addColorStop(0.45, 'rgba(176,97,22,' + a * 0.45 + ')'); g.addColorStop(1, 'rgba(176,97,22,0)');
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(px, py, r * 4, 0, 6.2832); ctx.fill();
      }
      ctx.globalCompositeOperation = 'source-over';
    }
    return { render: render };
  }

  window.MooreaLava = { create: create };
  window.MooreaEmbers = { create: createEmbers };
})();
