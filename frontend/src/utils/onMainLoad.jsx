export const onLoadUp = (useEffect, objClass, classShow) => {
    useEffect(() => {
        const animatedElements = document.querySelectorAll(objClass);
    
        const observer = new IntersectionObserver(entries => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.classList.add(classShow);
              observer.unobserve(entry.target);
            }
          });
        });
    
        animatedElements.forEach(el => {
          observer.observe(el);
        });
}, [])
}