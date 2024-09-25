def decode_message(s: str, p: str) -> bool:
    # Length of input string and pattern
    n, m = len(s), len(p)
    
    # Create a DP table with dimensions (n+1) x (m+1)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Base case: Empty pattern matches empty string
    dp[0][0] = True
    
    # Fill the first row where the pattern consists of only '*'
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the rest of the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                # If current chars match, or pattern has '?' (match one char)
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
    return dp[n][m]
