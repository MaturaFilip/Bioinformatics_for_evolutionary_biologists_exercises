#!/usr/bin/env python3


def per_aa_res(seq, aa = ['A', 'I', 'L', 'M', 'F', 'W','Y','V']):
        seq = seq.upper()
        seq_len = len(seq)
        res_count = 0
        for res in aa:
            res = res.upper()
            res_count += seq.count(res)

        return round((res_count / seq_len)*100)


assert per_aa_res("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert per_aa_res("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert per_aa_res("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert per_aa_res("MSRSLLLRFLLFLLLLPPLP") == 65
