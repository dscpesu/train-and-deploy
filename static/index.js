function post() {
  
  let v1 = Number(document.getElementById("val1").value);
  let v2 = Number(document.getElementById("val2").value);
  let v3 = Number(document.getElementById("val3").value);
  let v4 = Number(document.getElementById("val4").value);

  let reqObj = {
    method: 'POST',
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    },
    body: JSON.stringify([{
      "sepal length (cm)": v1,
      "sepal width (cm)": v2,
      "petal length (cm)": v3,
      "petal width (cm)": v4
    }]),
  }

  fetch("/predict", reqObj)
  .then(res=>res.json())
  .then((json)=>{
    let output = "Setosa"
    if(json.prediction == "[1]") {
      output="Versicolor"
    }
    if(json.prediction == "[2]") {
      output="Virginica"
    }
    document.getElementById("output").innerHTML = "The predicted Iris Class is " + output
  });

}

 
document.getElementById("sub").onclick = post;

