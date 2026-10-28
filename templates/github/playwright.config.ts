import { defineConfig, devices } from '@playwright/test';

const baseURL = process.env.E2E_BASE_URL;
if (!baseURL) throw new Error('Set E2E_BASE_URL to an explicitly authorized local/preview URL');
const target = new URL(baseURL);
if (!['https:', 'http:'].includes(target.protocol) || target.username || target.password) {
  throw new Error('Use an HTTP(S) target without embedded credentials');
}
if (target.protocol === 'http:' && !['localhost', '127.0.0.1', '[::1]'].includes(target.hostname)) {
  throw new Error('Remote previews must use HTTPS');
}
export default defineConfig({
  testDir: './tests/e2e',
  timeout: 30_000,
  workers: 1,
  retries: process.env.CI ? 1 : 0,
  use: { baseURL, trace: 'off', screenshot: 'off', video: 'off' },
  projects: [
    { name: 'chromium-desktop', use: { ...devices['Desktop Chrome'] } },
    { name: 'chromium-mobile', use: { ...devices['Pixel 7'] } },
  ],
  reporter: 'list',
});
