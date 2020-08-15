# Programmers Hash Practice Question
# Best Album
genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]


def solution(genres, plays):
    answer = []
    genre_dict = dict()
    genre_cnt = dict()
    bigFour = []
    for idx, genre in enumerate(genres):
        if not genre_dict.get(genre):
            genre_dict[idx] = [genre, plays[idx]]
            genre_cnt[genre] = 0
        genre_cnt[genre] += plays[idx]
    print(genre_dict)
    print(genre_cnt)
    for k,v in genre_dict.items():
        print(k,v)
    for v in sorted(genre_dict.values()):
        print(v)
    return answer


print(solution(genres, plays))


# def solution(genres, plays):
#     answer = []
#     countSong = dict()
#     idxDict = dict()
#     bigFour = []
#     for idx, genre in enumerate(genres):
#         if not countSong.get(genre):
#             countSong[genre] = 0
#             idxDict[genre] = dict()
#         countSong[genre] += plays[idx]
#         if not idxDict[genre].get(plays[idx]):
#             idxDict[genre][plays[idx]] = []
#         idxDict[genre][plays[idx]].append(idx)
#     print(idxDict)
#     print(countSong)


#     return answer


# print(solution(genres, plays))
