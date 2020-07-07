import streamlit as st
import joblib
import numpy as np

model=joblib.load('model.pkl')

def predict_house_price(crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat):
    input=np.array([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]]).astype(np.float64)
    predict=model.predict(input)
    return float(predict)

def main():
    html_temp = """
        <div style="background-color:#025246 ;padding:10px">
        <h2 style="color:white;text-align:center;">House Price Predictor </h2>
        </div>
         <br>
         <br>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    crim = st.text_input("Per capita crime rate", "Type Here")
    zn =st.text_input(" Proportion of residential land zoned for lots over 25,000 sq.ft.", "Type Here")
    indus = st.text_input("proportion of non-retail business acres per town", "Type Here")
    chas=st.text_input("House bounds charles river ? (= 1 if yes; 0 otherwise)","Type Here")
    nox= st.text_input("nitric oxides concentration (parts per 10 million)", "Type Here")
    rm = st.text_input(" average number of rooms per dwelling", "Type Here")
    age = st.text_input("proportion of owner-occupied units built prior to 1940", "Type Here")
    dis = st.text_input("weighted distances to five Boston employment centres", "Type Here")
    rad = st.text_input(" index of accessibility to radial highways", "Type Here")
    tax = st.text_input(" full-value property-tax rate per $10,000", "Type Here")
    ptratio = st.text_input("pupil-teacher ratio by town", "Type Here")
    b = st.text_input("1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town", "Type Here")
    lstat= st.text_input("% lower status of the population", "Type Here")



    if st.button("Predict"):
        output = predict_house_price(crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat)
        st.success(f'The predicted house price is {output} $1000s ')



if __name__=='__main__':
    main()




