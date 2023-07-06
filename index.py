from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
import yt_dlp

app = Flask(__name__)
# CORS(app)

@app.route("/")
def hello():
  return "Hello World!"


@app.route("/v1/get_video_info")
@cross_origin()
def getVideoInfo():
  args = request.args
  url = args['url']
  ydl = yt_dlp.YoutubeDL()
  try:
    data = ydl.extract_info(url, download=False)
    if data:
      return {
        "success": True,
        "data": data
      }
    else:
      return {
        "success": False
      }
  except:
    return {
      "success": False,
      "message": 'An error has occurred. Please try again later!'
    }


if __name__ == '__main__':
  app.run()
