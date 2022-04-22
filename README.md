# Iris-Flower-Detection-webapp

This is simple webapp made using Flask after creating a SVC(Support Vector Classifier) model on the iris dataset.

### **Link to Dataset:**

https://www.kaggle.com/datasets/arshid/iris-flower-dataset

### **Steps to try the project locally:**

1.  Download the project folder from my GitHub locally by directly downloading zip folder or 

    ```
      git clone https://github.com/Abdul-Hafeez-Galib/Iris-Flower-Detection-WebApp.git
    ```
    
2. 2. Open your Terminal and go to the directory of the folder.
3. Create a Virtual Environment for running Flask.

    ```
      py -3 -m venv venv
    ```
    
4. Activate the virtual environment.

    ```
      venv\scripts\activate
    ```
    
5. Install Flask in virtual environment.

    ```
      pip install flask
    ```
    
6. Run the flask app.

    ```
      set FLASK_APP=app.py
    ```
    
    ```
      flask run
    ```
    
7. Go to  http://127.0.0.1:5000 in a you browser to see the app working locally.
8. Input the features of the iris flower - Sepal length, Sepal width, Petal length and Petal width. Click Predict button.
9. See the prediction from the model if the iris flower is Iris-versicolor or Iris-setosa.

### **Images of WebApp:**

##### *Home Page*

![image](https://user-images.githubusercontent.com/77202232/164708860-3184f3a0-1350-4dd5-bd15-e11188318ecf.png)

##### *Result Page*

![image](https://user-images.githubusercontent.com/77202232/164708914-55252f4f-95ae-47de-a929-6bf52340dc90.png)
