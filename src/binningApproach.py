from abc import ABC, abstractmethod

class BinningApproach(ABC):
    @abstractmethod
    def binning(self, bin_size: int, min_bin: int = 0, max_bin: int = 10000):
        pass

    @abstractmethod
    def assign_colors(self, bin_size):
        pass


class DefaultBinningApproach(BinningApproach):
    def binning(self, bin_size: int, min_bin: int = 0, max_bin: int = 10000):
        """
        Dynamically generate range based buckets based on binning algorithm discussed in interview

        Args:
            bin_size (int): Number of bins to divide the range into.
            min_val (int): Minimum value of the range.
            max_val (int): Maximum value of the range.

        Returns:
            list of tuples: List of tuples where each tuple represents a bin range.

        """
        average = int((max_bin-min_bin)/bin_size)
        print(average)
        range_buckets = []
        start = min_bin
        for i in range(bin_size):
            cur_bin = start + average
            range_buckets.append((start+1, cur_bin))
            start = cur_bin

        return range_buckets

    def assign_colors(self, bin_size, color_code=1000):
        """
        Dynamically generate list of colors  based on binning size.
        Assuming color code is the actual color
        
        Args:
            bin_size (int): Number of bins to generate.
            color_code (int): Color code to be used from higher to lower weight of color.

        Returns:
            list of color code: List of Color code in increasing order  where color represents a bin range.

        """

        average = int(color_code/bin_size)
        colors = []
        for i in range(bin_size):
            colors.insert(0, color_code)
            color_code-=average

        return colors

if __name__=="__main__":
    """
    Testing Binning approach
    """
    binning_approach = DefaultBinningApproach()
    range_buckets = binning_approach.binning(5, 0, 5000)
    print(binning_approach.assign_colors(len(range_buckets)))

