def virusIndices(p, v):
    # Length of patient DNA
    n = len(p)
    # Length of virus DNA
    m = len(v)
    # List to store the starting indices of matching substrings
    result = []
    
    # Loop through each possible starting point in patient DNA
    for i in range(n - m + 1):
        # Counter for mismatches
        mismatch_count = 0
        # Loop through each character in virus DNA
        for j in range(m):
            # If characters do not match, increment mismatch count
            if p[i + j] != v[j]:
                mismatch_count += 1
            # If there are more than one mismatch, break out of the loop
            if mismatch_count > 1:
                break
        # If there is at most one mismatch, add starting index to result
        if mismatch_count <= 1:
            result.append(i)
    
    # If there are matching substrings, print their starting indices
    if result:
        print(' '.join(map(str, result)))
    # If no matching substrings, print "No match!"
    else:
        print("No match!")

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input().strip())

    # Loop through each test case
    for t_itr in range(t):
        # Read patient DNA and virus DNA for the current test case
        first_multiple_input = input().rstrip().split()

        p = first_multiple_input[0]
        v = first_multiple_input[1]

        # Call the virusIndices function for the current test case
        virusIndices(p, v)

