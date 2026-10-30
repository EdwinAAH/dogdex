import type { Breed } from "../types/breed";
import useBreedAnimation from "../hooks/useBreedAnimation";

import "./breedCard.css";

interface BreedCardProps {
  breed: Breed;
}

function BreedCard({ breed }: BreedCardProps) {
  const hasAnimation = useBreedAnimation(breed.slug);

  const spriteUrl = `/sprites/breeds/${breed.slug}.png`;
  const animationUrl = `/sprites/breeds/${breed.slug}-wag.png`;

  return (
    <article className="breed-card">
      <div className="breed-card__image">
        <div
          className={`breed-card__sprite ${
            hasAnimation ? "breed-card__sprite--animated" : ""
          }`}
          role="img"
          aria-label={`Sprite de ${breed.name}`}
          style={
            {
              "--sprite-url": `url("${spriteUrl}")`,
              "--animation-url": `url("${animationUrl}")`,
            } as React.CSSProperties
          }
        />
      </div>

      <div className="breed-card__info">
        <h3>{breed.name}</h3>

        <p>
          <strong>Origen:</strong> {breed.country.name}
        </p>

        <p>
          <strong>Tamaño:</strong> {breed.size_category}
        </p>
      </div>
    </article>
  );
}

export default BreedCard;