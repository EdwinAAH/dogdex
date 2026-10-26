import { useEffect, useState } from "react";

import BreedCard from "../components/breedCard";
import { getBreeds } from "../services/breedService";
import type { Breed } from "../types/breed";

function BreedListPage() {
  const [breeds, setBreeds] = useState<Breed[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadBreeds() {
      try {
        const response = await getBreeds();
        setBreeds(response.items);
      } catch {
        setError("No se pudieron cargar las razas.");
      } finally {
        setLoading(false);
      }
    }

    loadBreeds();
  }, []);

  if (loading) {
    return <p>Cargando razas... 🐕</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <main>
      <h1>🐕 DogDex</h1>
      <p>Explora el mundo de las razas caninas.</p>

      <h2>Razas disponibles</h2>

      {breeds.length === 0 ? (
        <p>Todavía no hay razas registradas.</p>
      ) : (
        <div className="breed-grid">
          {breeds.map((breed) => (
            <BreedCard key={breed.id} breed={breed} />
          ))}
        </div>
      )}
    </main>
  );
}

export default BreedListPage;