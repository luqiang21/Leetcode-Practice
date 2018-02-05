def compute(exp):
    stack = [];

    for v in exp:
      if type(v) == int:
        stack.append(v)
      else:
        b = stack.pop()
        a = stack.pop()

        if v == "+":
          stack.append(a + b)
        elif v == "-":
          stack.append(a - b)
        elif v == "*":
          stack.append(a * b)
        elif v == "/":
          stack.append(a / float(b))
        else:
          raise "Unsupported operator " + v

    return stack[0]


print(compute([ 6, 1, 3, 4, "/", "-", "/" ]))  # ==> 24

var operators = [ "+", "-", "*", "/" ];

// the function `solve` takes an array of numbers and an expected
// result (also a number).  It will find and print all expressions
// that contain the numbers exactly once and evaluate to that result.

function solve(numbers, result) {
    // returns true if `sol` is a solution to our problem
    function good_result(sol) {
        return compute(sol) == result;
    }

    // returns a list of things (numbers/operators) that are
    // valid to append to the current expression (`sol`).
    function next_choices(sol) {
        var available_numbers = numbers.filter(function(n){
            return sol.indexOf(n) < 0;
        });
        if (accepts_operator(sol))
            return operators.concat(available_numbers);
        return available_numbers;
    }

    // the main loop
    (function rec(sol){
        var things_to_try = next_choices(sol);
        if (things_to_try.length == 0) {
            if (good_result(sol))
                print(sol);
            fail();
        } else guess(things_to_try, function(value){
            rec(sol.concat(value));
        });
    })([]);
}
