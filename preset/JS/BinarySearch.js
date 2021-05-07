// 이진트리검색은 오름차순으로 정렬된 배열을 기반으로 
// 가운데 값을 이용하여 원하는 값을 찾아내는 검색 방법입니다.
function binarySearch(numArray, key) {
    var middleIdx = Math.floor(numArray.length / 2);
    var middleElem = numArray[middleIdx];

    if (middleElem === key) return true;
    else if (middleElem < key && numArray.length > 1) {
        return binarySearch(numArray.splice(middleIdx, numArray.length), key);
    }
    else if (middleElem > key && numArray.length > 1) {
        return binarySearch(numArray.splice(0, middleIdx), key);
    }
    else return false;
}