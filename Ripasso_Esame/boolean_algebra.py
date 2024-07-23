def evaluate_boolean_expression(expression):
    # Replace Boolean operators with their Python equivalents
    expression = expression.replace('AND', 'and')
    expression = expression.replace('OR', 'or')
    expression = expression.replace('NOT', 'not')

    try:
        # Evaluate the expression
        result = eval(expression)
        # Convert the result to binary (0 or 1)
        return 1 if result else 0
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

def main():
    print("Boolean Algebra Evaluator")
    print("Type 'exit' to quit the program.")
    while True:
        expression = input("Enter a Boolean expression: ")
        if expression.lower() == 'exit':
            break
        result = evaluate_boolean_expression(expression)
        if result is not None:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
