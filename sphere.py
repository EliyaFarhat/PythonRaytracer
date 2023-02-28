from math import sqrt
class Sphere:

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        """CHECKS IF RAY INTERSECTS THE SPHERE. RETURNS DISTANCE TO OR NONE IF NOT"""
        sphere_to_ray = ray.origin - self.center
        b = 2 * ray.direction.dotProduct(sphere_to_ray)
        c = sphere_to_ray.dotProduct(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            distance = (-b - sqrt(discriminant)) / 2
            if distance > 0:
                return distance
        return None

    def normal(self, surface_point):
        return (surface_point - self.center).normalize()