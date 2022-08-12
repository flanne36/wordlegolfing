


document.addEventListener("DOMContentLoaded", () => {
  createSquares();
  // getNewWord();

  let guessedWords = [[]];
  let availableSpace = 1;

  let word = data_from_django;
  let guessedWordCount = 0;
  let words = dictionary_from_django;

  let letterCorrectPosition = [];
  let indexCorrectPosition = [];

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

  function getTileColor(letter, index) {
    const isCorrectLetter = word.includes(letter);

    if (!isCorrectLetter) {
      return "rgb(58, 58, 60)";
    }

    const letterInThatPosition = word.charAt(index);
    const isCorrectPosition = letter === letterInThatPosition;

    if (isCorrectPosition) {
      letterCorrectPosition.push(letter);
      indexCorrectPosition.push(index);
      return "rgb(83, 141, 78)";
    }
    if(letterCorrectPosition.includes(letter)){
      for(let i = 0; i < word.length; i++){
        if(word.charAt(i) === letter && !indexCorrectPosition.includes(i)){
          return "rgb(83, 141, 78)";
        }
      }
      return "rgb(58, 58, 60)";
    }
    
    return "rgb(181, 159, 59)";
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
      currentWordArr.forEach((letter, index) => {
        setTimeout(() => {
          const tileColor = getTileColor(letter, index);
          const letterId = firstLetterId + index;
          const letterEl = document.getElementById(String(letterId));
          
          letterEl.classList.add("animate__flipInX");
          letterEl.style = `background-color: ${tileColor}; border-color: ${tileColor}`;

        }, interval * index);
      });

      setTimeout(() => {
        currentWordArr.forEach((letter, index) => {
          const tileColor = getTileColor(letter, index);
          const keyEl = document.getElementById(String(letter));
          keyEl.style = `background-color: ${tileColor}; border-color: ${tileColor}`;
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
