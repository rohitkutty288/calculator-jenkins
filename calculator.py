from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Calculator</title>
<style>
  :root{
    --bg:#0f1724;
    --panel:#0b1220;
    --key:#e6eef8;
    --key-muted:#c7d4e8;
    --accent:#ff8a00;
    --glass: rgba(255,255,255,0.03);
    --shadow: 0 6px 18px rgba(2,6,23,0.6);
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  }
  html,body{
    height:100%; 
    margin:0; 
    background: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e") no-repeat center center fixed;
    background-size: cover;
    display:flex; 
    align-items:center; 
    justify-content:center;
  }
  .wrap{width:360px; max-width:92vw; padding:28px; background:rgba(0,0,0,0.6); border-radius:18px; box-shadow:var(--shadow);}
  h1{color:var(--key-muted); font-weight:600; margin:0 0 12px 0; font-size:18px; text-align:center}
  .calculator{background:var(--panel); padding:18px; border-radius:14px; box-shadow: inset 0 -6px 14px rgba(2,6,23,0.6);}
  .display{
    height:72px; border-radius:10px; background:var(--glass); color:var(--key); font-size:28px; padding:12px;
    display:flex; align-items:center; justify-content:flex-end; box-sizing:border-box; margin-bottom:14px; overflow:hidden;
    border: 1px solid rgba(255,255,255,0.03);
  }
  .buttons{display:grid; grid-template-columns: repeat(4, 1fr); gap:10px;}
  button.key{
    padding:16px; border-radius:10px; border:0; font-size:18px; cursor:pointer; box-shadow: 0 6px 14px rgba(2,6,23,0.5);
    background: linear-gradient(180deg,#eef7ff, #dfeeff); color:#0b1a2b; user-select:none;
  }
  button.key:active{transform:translateY(1px); box-shadow: 0 2px 6px rgba(2,6,23,0.6);}
  button.op{ background: linear-gradient(180deg,#ff9b2e,#ff7a00); color:white; font-weight:600; }
  button.ctrl{ background: linear-gradient(180deg,#f3f7fb,#e6eef8); color:#0b1a2b; }
  button.wide{ grid-column: span 2; }
  .footer{ text-align:center; color:#7f99c0; margin-top:10px; font-size:12px;}
</style>
</head>
<body>
  <div class="wrap">
    <h1>Jenkins calculator</h1>
    <div class="calculator" role="application">
      <div class="display" id="display"><span id="expr">0</span></div>
      <div class="buttons">
        <button class="key ctrl" data-action="clear">C</button>
        <button class="key ctrl" data-action="neg">+/-</button>
        <button class="key ctrl" data-action="percent">%</button>
        <button class="key op" data-value="/">÷</button>
        <button class="key" data-value="7">7</button>
        <button class="key" data-value="8">8</button>
        <button class="key" data-value="9">9</button>
        <button class="key op" data-value="*">×</button>
        <button class="key" data-value="4">4</button>
        <button class="key" data-value="5">5</button>
        <button class="key" data-value="6">6</button>
        <button class="key op" data-value="-">−</button>
        <button class="key" data-value="1">1</button>
        <button class="key" data-value="2">2</button>
        <button class="key" data-value="3">3</button>
        <button class="key op" data-value="+">+</button>
        <button class="key wide" data-value="0">0</button>
        <button class="key" data-value=".">.</button>
        <button class="key op" data-action="equals">=</button>
      </div>
    </div>
    <div class="footer">Version 1.1</div>
  </div>

<script>
(function(){
  const display = document.getElementById('expr');
  let current = '0';

  function update(){ display.textContent = current; }
  function push(val){ if(current === '0' && val !== '.' ) current = val; else current += val; update(); }
  function clearAll(){ current = '0'; update(); }
  function toggleNeg(){ if(current.startsWith('-')) current = current.slice(1); else if(current !== '0') current = '-' + current; update(); }
  function percent(){ try{ current = String(evalExpression(current)/100); update(); }catch(e){} }
  function evalExpression(expr){
    expr = expr.replace(/÷/g, '/').replace(/×/g, '*').replace(/−/g, '-');
    if(!/^[0-9+\-*/(). %]+$/.test(expr)) throw new Error('Bad expression');
    return Function('"use strict"; return (' + expr + ')')();
  }
  function equals(){ try{ current = String(evalExpression(current)); update(); }catch(e){ current = 'Error'; update(); setTimeout(()=> clearAll(), 900); } }
  document.querySelectorAll('button.key').forEach(btn=>{
    btn.addEventListener('click', ()=> { const v = btn.dataset.value; const a = btn.dataset.action;
      if(a === 'clear') clearAll(); else if(a === 'neg') toggleNeg(); else if(a === 'percent') percent(); else if(a === 'equals') equals(); else if(v) push(v);
    });
  });
  document.addEventListener('keydown', (e)=>{
    if(e.key.match(/[0-9]/)) push(e.key);
    else if(e.key === '.') push('.');
    else if(e.key === 'Enter' || e.key === '=') equals();
    else if(e.key === 'Backspace'){ current = current.slice(0,-1) || '0'; update(); }
    else if(e.key === '+'||e.key==='-'||e.key==='*'||e.key==='/') push(e.key);
  });
  update();
})();
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
