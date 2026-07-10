class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
                return False
        l1=list(s1)
        l2=list(s2)

        left=0
        right=len(s1)

        ideal_window={}
        for ch in s1:
            ideal_window[ch]=ideal_window.get(ch,0)+1
        window={}

        for ch in s2[:right]:
            window[ch]=window.get(ch,0)+1
        if window==ideal_window:
                return True
        for ch in s2[right:]:
            

            window[ch]=window.get(ch,0)+1
            ch_lv=s2[left]
            window[ch_lv]-=1
            if window[ch_lv]==0:
                del window[ch_lv]

            left+=1
            if window==ideal_window:
                return True
        return False