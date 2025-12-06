import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n = len(courses)
        if n == 1:
            return 1
        
        # Sort courses by increasing order of end date
        sorted_courses = sorted(courses, key = lambda x: x[1])

        selection = [] # list of courses that we end up taking
        curr_time = 0

        for duration, last_day in sorted_courses:
            curr_time += duration
            heapq.heappush(selection, -duration)
            # If we cannot take all the courses in selection, remove the longest courses (and decrease curr_time) until everything fits.
            while curr_time > last_day:
                curr_time += heapq.heappop(selection)

        return len(selection)