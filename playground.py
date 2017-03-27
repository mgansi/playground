from flask import Flask, render_template
import serverInfo

app = Flask(__name__)


@app.route('/')
def index():
    info = serverInfo.ServerInfo.get_info()
    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run(debug=True)
