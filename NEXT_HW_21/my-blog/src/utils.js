export const getPostsFromLocalStorage = () => {
  const posts = localStorage.getItem('posts');
  return posts ? JSON.parse(posts) : [];
};

export const savePostsToLocalStorage = (posts) => {
  localStorage.setItem('posts', JSON.stringify(posts));
};

export const convertToBase64 = (file) => {
  return new Promise((resolve, reject) => {
      if (!file || !(file instanceof Blob)) {
          return reject(new Error('File is not a valid Blob.'));
      }

      const reader = new FileReader();
      reader.onloadend = () => {
          resolve(reader.result);
      };
      reader.onerror = reject;
      reader.readAsDataURL(file);
  });
};