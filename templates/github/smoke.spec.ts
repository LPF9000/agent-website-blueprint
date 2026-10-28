// Copy to tests/e2e/smoke.spec.ts and replace with site-specific acceptance journeys.
// Read-only: do not add production writes, login fixtures or form submission here.
import { test, expect } from '@playwright/test';

test('home has a successful response and visible main landmark', async ({ page }) => {
  const response = await page.goto('/');
  expect(response?.status()).toBe(200);
  await expect(page.getByRole('main')).toBeVisible();
  await expect(page).toHaveTitle(/\S/);
});
