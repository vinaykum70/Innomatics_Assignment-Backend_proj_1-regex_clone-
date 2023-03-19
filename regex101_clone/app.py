from flask import Flask, render_template , request
import re

app=Flask(__name__)

####################################################

@app.route('/', methods=['GET','POST'])
def home():
    try:

        target = request.args.get('target')
        regex = request.args.get('regex')

        if (target != None) and (regex != None):
            result = re.findall(regex, target)
            if result == ['']:
                result = ''
            length = len(result)

        else:
            result = ''
            length = 0

        return render_template('index.html', result=result, length=length, target=target , regex=regex)
    
    except Exception as e:
        print(e)

#############################################################

if __name__=='__main__':
    app.run(debug=True)




