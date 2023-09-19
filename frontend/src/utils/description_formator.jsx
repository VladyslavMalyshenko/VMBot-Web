//When the '/n' was found we'll return array with two or more items, in the opposite we'll return one item in the array
export const formatDescription = (descr) => {
    if (descr.includes('\n')) {
      return descr.split("\n");
    } else {
      return [descr];
    }
  };