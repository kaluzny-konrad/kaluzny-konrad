// https://www.codewars.com/kata/53dc23c68a0c93699800041d

function smash (words) {
    let sentence = "";

    for (const index in words) {
        let word = words[index];
        if(index > 0) sentence += " ";
        sentence += word;
    }
    
    return sentence;
};

module.exports = smash;