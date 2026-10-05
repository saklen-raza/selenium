// Simple Calculator - Experiment 11
function calculate(a, b, op) {
  switch (op) {
    case "add": return a + b;
    case "sub": return a - b;
    case "mul": return a * b;
    case "div":
      if (b === 0) throw new Error("Cannot divide by zero");
      return a / b;
  }
}

function showResult(op) {
  const n1 = document.getElementById("num1").value;
  const n2 = document.getElementById("num2").value;
  const result = document.getElementById("result");

  if (n1 === "" || n2 === "") {
    result.className = "err";
    result.textContent = "Please enter both numbers";
    return;
  }
  try {
    const value = calculate(parseFloat(n1), parseFloat(n2), op);
    result.className = "ok";
    result.textContent = "Result: " + value;
  } catch (e) {
    result.className = "err";
    result.textContent = "Error: " + e.message;
  }
}

["add", "sub", "mul", "div"].forEach(op => {
  document.getElementById(op).addEventListener("click", () => showResult(op));
});

document.getElementById("clear").addEventListener("click", () => {
  document.getElementById("num1").value = "";
  document.getElementById("num2").value = "";
  document.getElementById("result").textContent = "";
});