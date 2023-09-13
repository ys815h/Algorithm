# 2217 로프 (실버4)

N = int(input().strip())

st = []
for i in range(N):
    st.append(int(input().strip()))

length = len(st)
st.sort()

m_weight = st[0] * N
for j in range(1, len(st)):
    if m_weight < st[j] * (length - j):
        m_weight = st[j] * (length - j)

print(m_weight)