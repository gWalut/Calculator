from fastapi import FastAPI
app = FastAPI()


@app.post("/Calculator/{num1}/{num2}/{sign}")
def Calcult(num1: int,num2: int,sign: str):
    if sign=="+":
        return (num1+num2)
    if sign=="-":
        return (num1-num2)
    if sign=="*":
        return (num1*num2)
    if sign==":":
        if num2==0:
            return ("Error /0")
        return (num1/num2)
    return "error"