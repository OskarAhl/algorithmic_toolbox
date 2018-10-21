# Uses python3

# O(n) -- two consecutive loops
def has_majority_element(vote_list):
    # make dictionary of counts
    avg_total_count = len(vote_list) // 2
    votes_count = {}
    for vote in vote_list:
        if vote in votes_count:
            votes_count[vote] += 1
        else:
            votes_count[vote] = 1
    # loop hashmap to see if majority
    for key, value in votes_count.items():
        if value > avg_total_count:
            return 1
    return 0

if __name__ == '__main__':
    ignore = input()
    vote_list = [int(x) for x in input().split()]
    print(has_majority_element(vote_list))
