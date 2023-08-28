function generateHashtag(str: string): string | boolean {
    let phrase = str.replace(/\s+/g, " ").trim();
    if (!phrase || phrase.length >= 140) {
      return false;
    }
    let arrayWithTheFirstLetterUppercase = phrase.split(" ").map((word) => word[0].toUpperCase() + word.slice(1));
    return "#" + arrayWithTheFirstLetterUppercase.join("");
  }
  
  console.log(
    generateHashtag(
      "ABbCccDdddEeeeeFfffffGggggggHhhhhhhhGHGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    )
  );
  