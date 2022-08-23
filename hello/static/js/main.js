


document.addEventListener("DOMContentLoaded", () => {
  createSquares();

  let guessedWords = [[]];
  let availableSpace = 1;
  let guessedWordCount = 0;

  let word = data_from_django;
  let words = dictionary_from_django;
  let djangoGuessedWords = guessed_words_from_django;

  const messageDisplay = document.querySelector('.message-container')

  addDjangoGuessedWords();
  stats();

  console.log(word);

  function updatedstats() {
    if(guessedWordCount == 1) {
      oneWins++;
    } else if(guessedWordCount == 2) {
      twoWins++;
    } else if(guessedWordCount == 3) {
      threeWins++;
    } else if(guessedWordCount == 4) {
      fourWins++;
    } else if(guessedWordCount == 5) {
      fiveWins++;
    } else if(guessedWordCount == 6) {
      sixWins++;
    } else{
      losses++;
      curStreak = 0;
    }
    if(guessedWordCount < 7) {
      curStreak++;
      if(curStreak > maxStreak) {
        maxStreak = curStreak;
      }
    }
    
    played++;
    stats();
  }

  function stats() {
    document.getElementById("numOne").innerHTML = oneWins;
    document.getElementById("numTwo").innerHTML = twoWins;
    document.getElementById("numThree").innerHTML = threeWins;
    document.getElementById("numFour").innerHTML = fourWins;
    document.getElementById("numFive").innerHTML = fiveWins;
    document.getElementById("numSix").innerHTML = sixWins;
    document.getElementById("played").innerHTML = played;
    document.getElementById("curStreak").innerHTML = curStreak;
    document.getElementById("maxStreak").innerHTML = maxStreak;

    var percentage;
    if(losses == 0) {
      percentage = 100;
    } else {
      percentage = Math.round(((played - losses) / played) * 100);
    }

    var max = oneWins;
    if(twoWins > max) {
      max = twoWins;
    }
    if(threeWins > max) {
      max = threeWins;
    }
    if(fourWins > max) {
      max = fourWins;
    }
    if(fiveWins > max) {
      max = fiveWins;
    }
    if(sixWins > max) {
      max = sixWins;
    }
    var onePercent;
    var twoPercent;
    var threePercent;
    var fourPercent;
    var fivePercent;
    var sixPercent;

    if(max == 0){
      onePercent = 7;
      twoPercent = 7;
      threePercent = 7;
      fourPercent = 7;
      fivePercent = 7;
      sixPercent = 7;
      percentage = 0;
    } else {
      onePercent = oneWins / max * 100;
      if(onePercent < 7 || onePercent == 0) {
        onePercent = 7;
      }
      twoPercent = twoWins / max * 100;
      if(twoPercent < 7){
        twoPercent = 7;
      }
      threePercent = threeWins / max * 100;
      if(threePercent < 7){
        threePercent = 7;
      }
      fourPercent = fourWins / max * 100;
      if(fourPercent < 7){
        fourPercent = 7;
      }
      fivePercent = fiveWins / max * 100;
      if(fivePercent < 7){
        fivePercent = 7;
      }
      sixPercent = sixWins / max * 100;
      if(sixPercent < 7){
        sixPercent = 7;
      }
      
    }
    document.getElementById("percentage").innerHTML = percentage;
    
    var one = document.getElementById("one");
    one.style.width = onePercent + "%";
    var two = document.getElementById("two");
    two.style.width = twoPercent + "%";
    var three = document.getElementById("three");
    three.style.width = threePercent + "%";
    var four = document.getElementById("four");
    four.style.width = fourPercent + "%";
    var five = document.getElementById("five");
    five.style.width = fivePercent + "%";
    var six = document.getElementById("six");
    six.style.width = sixPercent + "%";
  }

  const keys = document.querySelectorAll(".keyboard-row button");

  function addDjangoGuessedWords() {
    for(let i = 0; i < djangoGuessedWords.length; i++) {
      let wordArr = Array.from(djangoGuessedWords[i]);
      for(let j = 0; j < wordArr.length; j++) {
        updateGuessedWords(wordArr[j]);
      }
      handleDjangoWord();
    }
  }

  function handleDjangoWord() {
    const currentWordArr = getCurrentWordArr();
    const currentWord = currentWordArr.join("");

    const firstLetterId = guessedWordCount * 5 + 1;
    const interval = 300;

    const colorsChoice = getTileColor(currentWord);

    currentWordArr.forEach((letter, index) => {
      setTimeout(() => {
        const letterId = firstLetterId + index;
        const letterEl = document.getElementById(String(letterId));
        
        letterEl.classList.add("animate__flipInX");
        if(colorsChoice[index] === 2){
          letterEl.style = `background-color: rgb(83, 141, 78); border-color: rgb(83, 141, 78)`;
        }else if(colorsChoice[index] === 1){
          letterEl.style = `background-color: rgb(181, 159, 59); border-color: rgb(181, 159, 59)`;
        }else{
          letterEl.style = `background-color: rgb(58, 58, 60); border-color: rgb(58, 58, 60)`;
        }
      }, interval * index);
    });
    const keyColorChoice = getKeyColor(currentWord);
    setTimeout(() => {
      currentWordArr.forEach((letter, index) => {
        const tileColor = getTileColor(letter, index);
        const keyEl = document.getElementById(String(letter));
        if(keyColorChoice[index] === 2){
          keyEl.style = `background-color: rgb(83, 141, 78); border-color: rgb(83, 141, 78)`;
        }else if(keyColorChoice[index] === 1){
          keyEl.style = `background-color: rgb(181, 159, 59); border-color: rgb(181, 159, 59)`;
        }else{
          keyEl.style = `background-color: rgb(58, 58, 60); border-color: rgb(58, 58, 60)`;
        }
      });
    }, interval * 5);


    guessedWordCount++;

  

    guessedWords.push([]);
  }

  function getCurrentWordArr() {
    const numberOfGuessedWords = guessedWords.length;
    return guessedWords[numberOfGuessedWords - 1];
  }

  function updateGuessedWords(letter) {
    const currentWordArr = getCurrentWordArr();

    if (currentWordArr && currentWordArr.length < 5) {
      currentWordArr.push(letter);

      const availableSpaceEl = document.getElementById(String(availableSpace));

      availableSpace = availableSpace + 1;
      availableSpaceEl.textContent = letter;
      availableSpaceEl.setAttribute("data-state", "tbd");
    }
  }

  function getTileColor(curWord){
    let answer = [0,0,0,0,0];
    let wordofday = word;
    for(let i = 0; i < curWord.length; i++){
      if(wordofday.charAt(i) === curWord.charAt(i)){
        answer[i] = 2;
        wordofday = wordofday.substring(0,i) + '_' + wordofday.substring(i+1);
        curWord = curWord.substring(0,i) + '*' + curWord.substring(i+1);
      }
    }
    for(let i = 0; i < curWord.length; i++){
      for(let j = 0; j < curWord.length; j++){
        if(curWord.charAt(i) === wordofday.charAt(j)){
          answer[i] = 1;
          wordofday = wordofday.substring(0,j) + '&' + wordofday.substring(j+1);
          j=6;
        }
      }
    }
    return answer;
  }

  function getKeyColor(curWord){
      let answer = [0,0,0,0,0];
      let wordofday = word;
      for(let i = 0; i < curWord.length; i++){
        if(wordofday.charAt(i) === curWord.charAt(i)){
          for(let j = 0; j < curWord.length; j++){
            if(curWord.charAt(j) === wordofday.charAt(i)){
              answer[j] = 2;
              curWord = curWord.substring(0,j) + '*' + curWord.substring(j+1);
            }
          }
        }
      }

      for(let i = 0; i < curWord.length; i++){
        if(wordofday.includes(curWord.charAt(i))){
          answer[i] = 1;
        }
      }
      return answer;
    }

  function handleSubmitWord() {
    const currentWordArr = getCurrentWordArr();
    if (currentWordArr.length !== 5) {
      showMessage("Not enough letters!");
    }

    const currentWord = currentWordArr.join("");


    if (words.includes(currentWord)) {

      const firstLetterId = guessedWordCount * 5 + 1;
      const interval = 200;

      const colorsChoice = getTileColor(currentWord);

      currentWordArr.forEach((letter, index) => {
        setTimeout(() => {
          const letterId = firstLetterId + index;
          const letterEl = document.getElementById(String(letterId));
          
          letterEl.classList.add("animate__flipInX");
          if(colorsChoice[index] === 2){
            letterEl.style = `background-color: rgb(83, 141, 78); border-color: rgb(83, 141, 78)`;
          }else if(colorsChoice[index] === 1){
            letterEl.style = `background-color: rgb(181, 159, 59); border-color: rgb(181, 159, 59)`;
          }else{
            letterEl.style = `background-color: rgb(58, 58, 60); border-color: rgb(58, 58, 60)`;
          }
        }, interval * index);
      });
      const keyColorChoice = getKeyColor(currentWord);
      setTimeout(() => {
        currentWordArr.forEach((letter, index) => {
          const tileColor = getTileColor(letter, index);
          const keyEl = document.getElementById(String(letter));
          if(keyColorChoice[index] === 2){
            keyEl.style = `background-color: rgb(83, 141, 78); border-color: rgb(83, 141, 78)`;
          }else if(keyColorChoice[index] === 1){
            keyEl.style = `background-color: rgb(181, 159, 59); border-color: rgb(181, 159, 59)`;
          }else{
            keyEl.style = `background-color: rgb(58, 58, 60); border-color: rgb(58, 58, 60)`;
          }
        });
      }, interval * 5);


      guessedWordCount++;

      if (currentWord === word) {
        updatedstats();
        saveCorrectAnswer();
        showCorrectMessage(guessedWordCount);
        setTimeout(() => {showStats();}, 2000);
      }else if (guessedWords.length === 6 && currentWord !== word) {
        guessedWordCount++;
        updatedstats();
        saveCorrectAnswer();
        showMessage(`You lost! The word is ${word}.`);
        setTimeout(() => {showStats();}, 2000);
      }else {
        saveGuess();
        guessedWords.push([]);
      }
      

    } else {
      showMessage("Not in word list");
    }
  }

  const showCorrectMessage = (guessedWordCount) => {
    const messageEl = document.createElement("p");
    if(guessedWordCount === 1){
      messageEl.textContent = "Hole In One!";
    }else if(guessedWordCount === 2){
      messageEl.textContent = "Eagle!";
    }else if(guessedWordCount === 3){
      messageEl.textContent = "Birdie!";
    }else if(guessedWordCount === 4){
      messageEl.textContent = "Par!";
    }else if(guessedWordCount === 5){
      messageEl.textContent = "Bogey!";
    }else if(guessedWordCount === 6){
      messageEl.textContent = "Double Bogey!";
    }
    messageDisplay.append(messageEl);
    setTimeout(() => {messageDisplay.removeChild(messageEl)}, 2000);
  }


  const showMessage = (message) => {
    const messageEl = document.createElement("p");
    messageEl.textContent = message;
    messageDisplay.append(messageEl);
    setTimeout(() => messageDisplay.removeChild(messageEl), 2000);
  }

  function saveGuess(){
    const currentWordArr = getCurrentWordArr();
    const currentWord = currentWordArr.join("");
    const w = JSON.stringify(currentWord);
    $.ajax({
      url: '/game/saveguess/',
      type: 'POST',
      data: w
    });
  }

  function saveCorrectAnswer() {
    const currentWordArr = getCurrentWordArr();
    const currentWord = currentWordArr.join("");
    const w = JSON.stringify(currentWord);
    $.ajax({
      url: "/game/stats/",
      type: "POST",
      data: {wordCount : JSON.stringify(guessedWordCount), word : w}
    });
  }

  function createSquares() {
    const gameBoard = document.getElementById("board");

    for (let index = 0; index < 30; index++) {
      let square = document.createElement("div");
      square.classList.add("square");
      square.classList.add("animate__animated");
      square.setAttribute("id", index + 1);
      square.setAttribute("data-state", "empty");
      gameBoard.appendChild(square);
    }
  }

  function handleDeleteLetter() {
    const currentWordArr = getCurrentWordArr();
    if (currentWordArr.length > 0) {
      const removedLetter = currentWordArr.pop();

      guessedWords[guessedWords.length - 1] = currentWordArr;

      const lastLetterEl = document.getElementById(String(availableSpace - 1));

      lastLetterEl.textContent = "";
      availableSpace = availableSpace - 1;
      lastLetterEl.setAttribute("data-state", "empty");
    }
  }

  for (let i = 0; i < keys.length; i++) {
    keys[i].onclick = ({ target }) => {
      const letter = target.getAttribute("data-key");
      if (letter === "enter") {
        handleSubmitWord();
        return;
      }

      if (letter === "del") {
        handleDeleteLetter();
        return;
      }

      updateGuessedWords(letter);
    };
  }

  document.addEventListener("keydown", ( event ) => {
    var name = event.key;
    var code = event.keyCode;
    if (name === "Enter") {
      handleSubmitWord();
      return;
    }
    if (name === "Backspace") {
      handleDeleteLetter();
      return;
    }
    if (/^[a-zA-Z]$/.test(name)) {
      updateGuessedWords(name.toLocaleLowerCase());
    }
  }, false);
});