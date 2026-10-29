
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        required_counts = {}
        window_counts = {}

        for char in t:
            required_counts[char] = required_counts.get(char, 0) + 1

        matched_chars = 0
        required_chars = len(required_counts)

        min_window = [-1, -1]
        min_window_length = float("inf")

        left = 0

        for right in range(len(s)):
            current_char = s[right]
            window_counts[current_char] = window_counts.get(current_char, 0) + 1

            if (
                current_char in required_counts
                and window_counts[current_char] == required_counts[current_char]
            ):
                matched_chars += 1

            while matched_chars == required_chars:
                current_window_length = right - left + 1

                if current_window_length < min_window_length:
                    min_window = [left, right]
                    min_window_length = current_window_length

                left_char = s[left]

                window_counts[left_char] -= 1

                if (
                    left_char in required_counts
                    and window_counts[left_char] < required_counts[left_char]
                ):
                    matched_chars -= 1

                left += 1

        start, end = min_window

        if min_window_length == float("inf"):
            return ""

        return s[start:end + 1]
