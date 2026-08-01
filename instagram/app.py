
from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Página</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: #fafafa;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      text-align: center;
    }

    h1 {
      color: #333;
      margin-bottom: 10px;
    }

    p {
      color: #666;
      margin-bottom: 30px;
    }

    .btn-instagram {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 14px 28px;
      background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
      color: white;
      text-decoration: none;
      font-weight: bold;
      font-size: 16px;
      border-radius: 30px;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .btn-instagram:hover {
      transform: scale(1.05);
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
  </style>
</head>
<body>

  <h1>¡Seguime en Instagram!</h1>
  <p>Hacé clic en el botón para ir a mi perfil.</p>

  <a href="https://www.instagram.com/maxipimenttel" target="_blank" class="btn-instagram">
     "Ir a mi perfil" 
  </a>

</body>
</html>
"""


@app.route("/")
def home():
    return HTML_PAGE


if __name__ == "__main__":
    app.run(debug=True)