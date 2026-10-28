# Accessibility

## Purpose

Make essential journeys usable with keyboards, assistive technology, different vision and device sizes.

## When needed

Every website. Treat accessibility as acceptance criteria from planning onward.

## Prerequisites

Page/journey inventory, representative content, browser devtools and access to a keyboard/screen reader. Document a WCAG 2.2 AA engineering target and any jurisdiction-specific review needs.

## Recommended implementation

Use native HTML controls and semantic structure. Combine automated audits with manual keyboard/screen-reader testing; an automated score is incomplete evidence and does not certify compliance.

## Setup

1. Use one main landmark, logical headings, skip navigation, meaningful page titles and descriptive link/button text. Set page language.
2. Make every action keyboard accessible with visible focus and sensible focus order. Test menu/dialog focus management, Escape behavior, restoration and prevention of keyboard traps.
3. Label form fields programmatically; identify required fields, instructions and errors in text, associate them with inputs and announce async outcomes appropriately. Do not use placeholder text as the only label.
4. Provide meaningful alt text for informative images, empty alt for decorative images, captions/transcripts for relevant media and non-visual alternatives for essential charts.
5. Verify text/UI contrast, zoom/reflow, touch target spacing, reduced-motion preference and information that does not rely on color alone. Test at 200% zoom and narrow/reflow conditions.
6. Run Lighthouse/axe for representative public and authenticated templates in isolated preview; address serious issues. Use Playwright role/label locators to reinforce semantic contracts.
7. Manually complete core journeys using keyboard and a screen reader (for example VoiceOver or NVDA), including validation failures, calendar controls and admin dialogs. Record tested browser/device and remaining issues.

## Security considerations

Accessible authentication, error messaging and recovery matter. Do not expose private values through accessible labels, hidden test data or screen-reader-only elements. Bot protection must have usable failure/retry paths.

## Free-tier limitations

Native HTML, browser tools and open-source auditing tools can be free. Paid audits are optional unless required by risk/contract. Screen-reader/browser coverage and expert review still require human time.

## Verification

Acceptance includes a full keyboard journey, readable focus, correct names/roles, no serious automated findings on key templates and manual screen-reader observations. Record gaps honestly; “Lighthouse 100” alone is not acceptance.

## Troubleshooting

If an ARIA widget is difficult to implement, prefer a native control. Missing announcements: inspect live-region timing and error association. Off-screen content: check zoom, overflow and fixed widths rather than adding horizontal scroll everywhere.

## Official documentation

[WCAG 2.2](https://www.w3.org/TR/WCAG22/) · [WAI tutorials](https://www.w3.org/WAI/tutorials/) · [WAI evaluation](https://www.w3.org/WAI/test-evaluate/) · [Playwright accessibility](https://playwright.dev/docs/accessibility-testing)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
