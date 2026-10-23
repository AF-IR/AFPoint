bash -lc cat > /mnt/data/arsham_point_traffic.html <<'EOF'
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#07132e">
<title>Arsham Point | ترافیک شدید</title>
<style>
:root {
  --site-primary: #386bff;
  --site-secondary: #8b42f5;
  --site-background: #07132e;
  --site-on-primary: #ffffff;
  --site-on-secondary: #ffffff;
  --site-on-background: #f5f7ff;
  --site-font-body: Tahoma, "Segoe UI", sans-serif;
  --site-font-heading: Tahoma, "Segoe UI", sans-serif;
  --site-heading-scale: 1;
  --site-spacing-scale: 1;
  --site-radius-scale: 1;
  --site-decoration-opacity: 1;
  color-scheme: light dark;
}
* { box-sizing: border-box; }
html, body { margin: 0; min-height: 100%; }
body { font-family: var(--site-font-body); background: var(--site-background); color: var(--site-on-background); }
#app { min-height: 100vh; width: 100%; border-radius: 0; overflow: hidden; position: relative; isolation: isolate; background: radial-gradient(ellipse at 80% 10%, #31216c 0, transparent 35%), radial-gradient(ellipse at 12% 80%, #063f69 0, transparent 38%), var(--site-background); }
.decor { position: absolute; inset: 0; pointer-events: none; opacity: var(--site-decoration-opacity); overflow: hidden; z-index: -1; }
.orb { position: absolute; border-radius: 50%; filter: blur(2px); opacity: .28; }
.orb.one { width: 360px; height: 360px; background: #713cff; top: -180px; right: -90px; }
.orb.two { width: 280px; height: 280px; background: #00b9ff; bottom: -160px; left: -90px; }
.grid { position: absolute; inset: 0; background-image: linear-gradient(#8eacff10 1px, transparent 1px), linear-gradient(90deg, #8eacff10 1px, transparent 1px); background-size: 44px 44px; mask-image: linear-gradient(to bottom, black, transparent 90%); }
.wrap { width: min(1100px, 100%); margin: auto; padding: calc(28px * var(--site-spacing-scale)) calc(22px * var(--site-spacing-scale)) 34px; }
header { display: flex; align-items: center; justify-content: space-between; gap: 18px; }
.brand { display: flex; align-items: center; gap: 13px; font-family: var(--site-font-heading); font-size: calc( clamp(22px, 4vw, 34px) * var(--site-heading-scale)); font-weight: 900; letter-spacing: -.8px; }
.brand-mark { width: 46px; height: 46px; display: grid; place-items: center; border-radius: calc(15px * var(--site-radius-scale)); background: linear-gradient(135deg, var(--site-primary), var(--site-secondary)); box-shadow: 0 0 30px #633eff70; font-size: 28px; color: white; }
.brand span span { color: #52c7ff; }
.pill { border: 1px solid #ffc45b70; color: #ffd58b; background: #ffb52a12; border-radius: 999px; padding: 9px 14px; font-size: 13px; white-space: nowrap; }
main { display: grid; grid-template-columns: 1.1fr .9fr; align-items: center; gap: 42px; padding: 70px 0 45px; }
.eyebrow { color: #74d5ff; font-weight: 700; font-size: 14px; letter-spacing: .4px; }
h1 { font-family: var(--site-font-heading); font-size: calc(clamp(34px, 5.6vw, 62px) * var(--site-heading-scale)); line-height: 1.32; margin: 15px 0 20px; letter-spacing: -1.5px; }
h1 em { font-style: normal; background: linear-gradient(90deg, #55d7ff, #a66aff 80%); -webkit-background-clip: text; background-clip: text; color: transparent; }
.lead { color: #c3cde9; font-size: clamp(16px, 2vw, 19px); line-height: 2; max-width: 610px; margin: 0; }
.notice { display: flex; gap: 13px; align-items: flex-start; margin-top: 27px; padding: 17px; border: 1px solid #6b7eff4a; border-radius: calc(18px * var(--site-radius-scale)); background: #101f45b8; }
.notice-icon { flex: 0 0 40px; height: 40px; display: grid; place-items: center; border-radius: 13px; background: #ffb54720; color: #ffc56a; font-size: 23px; }
.notice strong { display: block; margin-bottom: 6px; font-size: 15px; }
.notice p { margin: 0; color: #aebbdc; font-size: 13px; line-height: 1.9; }
.panel { position: relative; padding: 28px; border: 1px solid #a3b7ff38; border-radius: calc(28px * var(--site-radius-scale)); background: linear-gradient(145deg, #17264dcc, #0a1633e8); box-shadow: 0 24px 80px #0007, inset 0 1px #ffffff12; text-align: center; }
.panel:before { content: ""; position: absolute; inset: -1px; border-radius: inherit; padding: 1px; background: linear-gradient(135deg, #55d7ff88, transparent 40%, #a35dff88); -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); -webkit-mask-composite: xor; mask-composite: exclude; pointer-events: none; }
.pulse { width: 84px; height: 84px; margin: 0 auto 18px; border-radius: 26px; display: grid; place-items: center; background: linear-gradient(135deg, #256bff, #9c4bff); box-shadow: 0 0 42px #7248ff65; font-size: 40px; animation: float 3s ease-in-out infinite; }
@keyframes float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-7px); } }
.panel h2 { font-size: 21px; margin: 0 0 9px; }
.panel .sub { color: #aebbdc; font-size: 13px; margin: 0 0 23px; }
.counter { direction: ltr; font-variant-numeric: tabular-nums; font-size: clamp(52px, 7vw, 76px); font-weight: 900; letter-spacing: 3px; line-height: 1.2; background: linear-gradient(90deg, #55d7ff, #a777ff); -webkit-background-clip: text; background-clip: text; color: transparent; text-shadow: 0 0 32px #5d74ff35; }
.counter-label { margin-top: 9px; color: #dfe6ff; font-weight: 700; font-size: 14px; }
.live { display: inline-flex; align-items: center; gap: 8px; margin-top: 19px; color: #8fe8c3; font-size: 12px; background: #35d49b12; border: 1px solid #35d49b45; border-radius: 999px; padding: 8px 12px; }
.live i { width: 7px; height: 7px; display: inline-block; border-radius: 50%; background: #5be0a8; box-shadow: 0 0 10px #5be0a8; }
.progress { height: 6px; background: #ffffff12; border-radius: 99px; margin-top: 24px; overflow: hidden; }
.progress span { display: block; height: 100%; width: 84%; border-radius: inherit; background: linear-gradient(90deg, #4bd6ff, #9854ff); animation: breathe 2.5s ease-in-out infinite alternate; }
@keyframes breathe { from { width: 76%; } to { width: 91%; } }
footer { border-top: 1px solid #9ab0ff25; padding-top: 23px; display: flex; align-items: center; justify-content: space-between; gap: 15px; color: #8f9fc6; font-size: 12px; }
footer strong { color: #dce6ff; }
.url { direction: ltr; color: #79d9ff; text-decoration: none; font-weight: 700; }
@media (max-width: 760px) { .wrap { padding-top: 20px; } header { align-items: flex-start; } .pill { font-size: 11px; padding: 8px 10px; } .brand-mark { width: 40px; height: 40px; font-size: 24px; } main { grid-template-columns: 1fr; gap: 30px; padding: 52px 0 34px; } .intro { text-align: center; } .lead { margin-inline: auto; } .notice { text-align: right; } .panel { max-width: 440px; width: 100%; margin: auto; padding: 25px 18px; } footer { flex-direction: column; text-align: center; } }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; scroll-behavior: auto !important; } }
</style>
</head>
<body>
<div id="app" data-sites-preview-theme="custom">
  <div class="decor" aria-hidden="true"><div class="grid"></div><div class="orb one"></div><div class="orb two"></div></div>
  <div class="wrap">
    <header>
      <div class="brand"><div class="brand-mark">A</div><div>Arsham <span>Point</span></div></div>
      <div class="pill">● اطلاعیه وضعیت سرویس</div>
    </header>
    <main>
      <section class="intro">
        <div class="eyebrow">یک لحظه صبر کنید؛ داریم آماده می‌شویم</div>
        <h1>ترافیک شدید در<br><em>ساخت پرده‌نگار</em><br>آرشام پوینت</h1>
        <p class="lead">به‌دلیل استقبال زیاد کاربران، درخواست‌های ساخت ارائه با هوش مصنوعی بیشتر از حد معمول شده است. در حال مدیریت ترافیک هستیم تا تجربه‌ای بهتر و پایدارتر داشته باشید.</p>
        <div class="notice"><div class="notice-icon">✦</div><div><strong>نگران نباشید، به‌زودی برمی‌گردیم</strong><p>لطفاً چند لحظه دیگر دوباره تلاش کنید. از صبوری و همراهی شما ممنونیم.</p></div></div>
      </section>
      <aside class="panel" aria-label="شمارنده درخواست‌های هم‌زمان">
        <div class="pulse">✧</div>
        <h2>آرشام پوینت در حال پردازش است</h2>
        <p class="sub">تعداد نمایشی درخواست‌های هم‌زمان ساخت</p>
        <div class="counter" id="count" aria-live="polite">۴۶۸</div>
        <div class="counter-label">درخواست هم‌زمان ساخت</div>
        <div class="live"><i></i> سامانه در حالت مدیریت ترافیک</div>
        <div class="progress" aria-hidden="true"><span></span></div>
      </aside>
    </main>
    <footer><div><strong>Arsham Point</strong> — ابزار هوشمند ساخت و طراحی ارائه</div><a class="url" href="https://afpoint.vercel.app">AFpoint.vercel.app</a></footer>
  </div>
</div>
<script>
// این شمارنده صرفاً نمایشی است و از سرور یا آمار واقعی درخواست‌ها داده نمی‌گیرد.
(() => {
  const el = document.getElementById('count');
  let value = Math.floor(Math.random() * 101) + 400;
  const fa = new Intl.NumberFormat('fa-IR');
  el.textContent = fa.format(value);
  setInterval(() => {
    value += Math.floor(Math.random() * 7) - 3;
    if (value < 400) value = 400 + Math.floor(Math.random() * 4);
    if (value > 500) value = 496 + Math.floor(Math.random() * 5);
    el.textContent = fa.format(value);
  }, 4200);
})();
</script>
</body>
</html>
EOF
wc -c /mnt/data/arsham_point_traffic.html
