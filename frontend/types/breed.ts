export interface Country {
  id: number;
  name: string;
}

export interface BreedGroup {
  id: number;
  name: string;
}

export interface BreedImage {
  image_url: string;
  source_url: string | null;
  author: string | null;
  license: string | null;
  alt_text: string;
}

export type BreedSize = "small" | "medium" | "large" | "giant";

export interface Breed {
  id: string;
  name: string;
  slug: string;

  country_id: number;
  group_id: number;

  country: Country;
  group: BreedGroup;

  coat_types: string[];

  images: BreedImage[];
  primary_image: BreedImage | null;

  male_height_min_cm: number | null;
  male_height_max_cm: number | null;
  female_height_min_cm: number | null;
  female_height_max_cm: number | null;

  male_weight_min_kg: number | null;
  male_weight_max_kg: number | null;
  female_weight_min_kg: number | null;
  female_weight_max_kg: number | null;

  lifespan_min_years: number | null;
  lifespan_max_years: number | null;

  size_category: BreedSize;

  original_purpose: string | null;
  description: string | null;
  history: string | null;

  created_at: string;
  updated_at: string;
}

export interface BreedListResponse {
  total: number;
  limit: number;
  offset: number;
  items: Breed[];
}