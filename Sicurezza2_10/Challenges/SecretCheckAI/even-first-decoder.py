def decode_interleaved_even_first(encoded_string):
    # Get characters at odd positions (indices 0, 2, 4, ...)
    odd_positions = encoded_string[::2]
    
    # Get characters at even positions (indices 1, 3, 5, ...)
    even_positions = encoded_string[1::2]
    
    # Combine even positions first, then odd positions
    result = even_positions + odd_positions
    
    print(f"Original string: {encoded_string}")
    print(f"Length: {len(encoded_string)} characters")
    print("\nOdd positions (0-indexed):")
    print(odd_positions)
    print(f"Length: {len(odd_positions)} characters")
    print("\nEven positions (0-indexed):")
    print(even_positions)
    print(f"Length: {len(even_positions)} characters")
    print("\nFinal result (even + odd):")
    print(result)
    
    # Also try with reversed even positions
    reversed_even = even_positions[::-1]
    alt_result = reversed_even + odd_positions
    print("\nAlternative result (reversed even + odd):")
    print(alt_result)
    
    return result, alt_result

# Your encoded string
encoded_string = "it04nd_11ls4_vn_33vd31rs__tthn33_1sl0cl{uCtE1S0AnT!I}"

# Run the decoder
result, alt_result = decode_interleaved_even_first(encoded_string)
