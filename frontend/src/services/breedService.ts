import type { Breed, BreedListResponse } from "../types/breed";

const API_URL = import.meta.env.VITE_API_URL;

export async function getBreeds(): Promise<BreedListResponse> {
  const response = await fetch(`${API_URL}/breeds`);

  if (!response.ok) {
    throw new Error("No se pudieron obtener las razas");
  }

  return response.json();
}

export async function getBreedBySlug(slug: string): Promise<Breed> {
  const response = await fetch(
    `${API_URL}/breeds/${encodeURIComponent(slug)}`
  );

  if (!response.ok) {
    throw new Error(`No se pudo obtener la raza: ${slug}`);
  }

  return response.json();
}