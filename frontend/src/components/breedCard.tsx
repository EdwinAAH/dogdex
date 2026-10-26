import type { Breed } from "../types/breed";
import "./breedCard.css";

interface BreedCardProps {
  breed: Breed;
}

function BreedCard({ breed }: BreedCardProps) {
  return (
    <article className="breed-card">
      <div className="breed-card__image">
        <img
          src={`/sprites/breeds/${breed.slug}.png`}
          alt={`Sprite de ${breed.name}`}
          width={120}
          height={120}
          loading="lazy"
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