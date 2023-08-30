import streamlit as st

def largest(n1,n2,n3):
    mx = (n1 if (n1 > n2 and n1 > n3) else
          (n2 if (n2 > n1 and n2 > n3) else n3))
    return mx

def main():
    st.title('Find the largest number ')
    num1=st.number_input("Enter first number ")
    num2=st.number_input("Enter second number ")
    num3=st.number_input("Enter third number ")

    if st.button("Find Largest"):
        st.write("Largest number among " + str(num1) + ", " + str(num2) + " and " + str(num3) + " is " + str(largest(num1,num2,num3)))

if __name__ == '__main__':
    main()