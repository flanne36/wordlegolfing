


document.addEventListener("DOMContentLoaded", () => {
  createSquares();
  // getNewWord();

  let guessedWords = [[]];
  let availableSpace = 1;

  let word = data_from_django;
  let guessedWordCount = 0;
  let words = dictionary_from_django;

  console.log(word);

  const keys = document.querySelectorAll(".keyboard-row button");

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
      console.log(wordofday);
      console.log(curWord);
      console.log(answer);

      for(let i = 0; i < curWord.length; i++){
        if(wordofday.includes(curWord.charAt(i))){
          answer[i] = 1;
        }
      }
      console.log(wordofday);
      console.log(curWord);
      console.log(answer);
      return answer;
    }

  function handleSubmitWord() {
    const currentWordArr = getCurrentWordArr();
    if (currentWordArr.length !== 5) {
      window.alert("Word must be 5 letters");
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
       // window.alert("You guessed the word!");
        console.log("You guessed the word!");
        saveCorrectAnswer();
      }
      
      if (guessedWords.length === 6) {
        window.alert(`You lost! The word is ${word}.`);
        guessedWordCount++;
        saveCorrectAnswer();
      }

      guessedWords.push([]);
    } else {
      window.alert("Word not in list");
    }
  }

  function saveCorrectAnswer() {
    const currentWordArr = getCurrentWordArr();
    const currentWord = currentWordArr.join("");
    const w = JSON.stringify(currentWord);
    $.ajax({
      url: "/game/stats/",
      type: "POST",
      data: JSON.stringify(guessedWordCount)
    });
  }

  function createSquares() {
    const gameBoard = document.getElementById("board");

    for (let index = 0; index < 30; index++) {
      let square = document.createElement("div");
      square.classList.add("square");
      square.classList.add("animate__animated");
      square.setAttribute("id", index + 1);
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
});
