def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    merged = [0] * (m+n)
    cnt1 = 0
    cnt2 = 0
    m_cnt = 0
    while m_cnt < m+n:
        if cnt1 == m:
            for i in range(cnt2, n):
                merged[m_cnt] = nums2[cnt2]
                cnt2 += 1
                m_cnt += 1
            break
        elif cnt2 == n:
            for i in range(cnt1, m):
                merged[m_cnt] = nums1[cnt1]
                cnt1 += 1
                m_cnt += 1
            break
        if nums1[cnt1] <= nums2[cnt2]:
            merged[m_cnt] = nums1[cnt1]
            cnt1 += 1
        elif nums1[cnt1] > nums2[cnt2]:
            merged[m_cnt] = nums2[cnt2]
            cnt2 += 1
        m_cnt += 1
    for i in range(m+n):
        nums1[i] = merged[i]