// https://www.codewars.com/kata/53dc23c68a0c93699800041d

function smash (words) {
    let sentence = "";
    for (const index in words)
        sentence += getWord(words[index], index);
    return sentence;
};

function getWord(word, index) {
    if(index > 0) return " " + word;
    else return word;
}

module.exports = smash;