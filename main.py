from flask import Flask,render_template
import pickle
app=Flask(__name__)


with open ("popular_50_books.pkl","rb") as file:
    popular_50_books=pickle.load(file)



@app.route("/")
def home():
    return render_template("index.html",book_name=list(popular_50_books["Book-Title"].values),
                                                      Author=list(popular_50_books["Book-Author"].values), 
                                                      Year=list(popular_50_books["Year-Of-Publication"].values),
                                                      
                                                      image=list(popular_50_books["Image-URL-M"].values))



if __name__=="__main__":

    app.run(debug=True)


