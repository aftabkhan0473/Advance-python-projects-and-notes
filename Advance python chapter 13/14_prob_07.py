from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_world():
    return '''Q itna hua hai tu khafa hai dar kis baat ki teri ki maregi jyada mujhe maut se narajagi teri janisar hai janisar 
    tere pyar ka mere yar jaannisar hai oh q itna hua hai tu khafa hai dar kis baat ki teri ki maregi jyada mujhe maut se narajagi ter
    
    '''
if __name__ == "__main__":
    app.run(debug=True)