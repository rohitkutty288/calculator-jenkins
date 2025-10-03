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
    --panel: rgba(255, 255, 255, 0.85); /* semi-transparent panel */
    --key:#0b1a2b;
    --key-muted:#1a1a1a;
    --accent:#4285F4; /* Google Blue */
    --glass: rgba(255,255,255,0.3);
    --shadow: 0 6px 18px rgba(0,0,0,0.6);
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  }

  html,body{
    height:100%;
    margin:0;
    /* Google office image background */
    background: url("https://upload.wikimedia.org/wikipedia/commons/5/5f/Googleplex_HQ_%28cropped%29.jpg") no-repeat center center fixed;
    background-size: cover;
    display:flex;
    align-items:center;
    justify-content:center;
  }

  .wrap{
    width:360px;
    max-width:92vw;
    padding:28px;
    background: var(--panel);
    border-radius:18px;
    box-shadow:var(--shadow);
    backdrop-filter: blur(10px);
  }

  h1{
    color:var(--key-muted);
    font-weight:600;
    margin:0 0 12px 0;
    font-size:18px;
    text-align:center
  }

  .calculator{
    background: rgba(255,255,255,0.9);
    padding:18px;
    border-radius:14px;
    box-shadow: inset 0 -6px 14px rgba(0,0,0,0.2);
  }

  .display{
    height:72px;
    border-radius:10px;
    background:var(--glass);
    color:var(--key);
    font-size:28px;
    padding:12px;
    display:flex;
    align-items:center;
    justify-content:flex-end;
    box-sizing:border-box;
    margin-bottom:14px;
    overflow:hidden;
    border: 1px solid rgba(0,0,0,0.1);
  }

  .buttons{display:grid; grid-template-columns: repeat(4, 1fr); gap:10px;}
  button.key{
    padding:16px;
    border-radius:10px;
    border:0;
    font-size:18px;
    cursor:pointer;
    box-shadow: 0 6px 14px rgba(0,0,0,0.2);
    background: linear-gradient(180deg,#e8e8e8, #f2f2f2);
    color:#0b1a2b;
    user-select:none;
  }
  button.key:active{transform:translateY(1px); box-shadow: 0 2px 6px rgba(0,0,0,0.3);}
  button.op{ background: var(--accent); color:white
