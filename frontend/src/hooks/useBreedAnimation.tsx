import { useEffect, useState } from "react";

function useBreedAnimation(slug: string) {
  const [hasAnimation, setHasAnimation] = useState(false);

  useEffect(() => {
    let active = true;

    setHasAnimation(false);

    const image = new Image();

    image.onload = () => {
      if (active) {
        setHasAnimation(true);
      }
    };

    image.onerror = () => {
      if (active) {
        setHasAnimation(false);
      }
    };

    image.src = `/sprites/breeds/${slug}-wag.png`;

    return () => {
      active = false;
    };
  }, [slug]);

  return hasAnimation;
}

export default useBreedAnimation;