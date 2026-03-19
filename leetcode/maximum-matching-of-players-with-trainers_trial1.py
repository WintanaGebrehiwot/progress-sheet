class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        count = 0
        first, second = 0, 0
        while first < len(players) and second < len(trainers):
            if players[first] <= trainers[second]:
                count += 1
                first += 1
                second += 1
            else:
                second += 1
        
        return count

        
        