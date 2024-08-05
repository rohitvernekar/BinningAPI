
from binningApproach import BinningApproach

class BinningService:
    """
    Service to handle binning related functionality
    """
    def __init__(self, approach: BinningApproach):
        self.bin_object = approach

    def process_binning_data(self, bin_size, min_val, max_val):
        binning_buckets = self.bin_object.binning(bin_size=bin_size, min_bin=min_val, max_bin=max_val)
        num_bins = len(binning_buckets)
        bin_wise_colors = self.bin_object.assign_colors(num_bins)
        return {
            'range_buckets': binning_buckets,
            'buckets_color': bin_wise_colors
        } 


