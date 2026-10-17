// Contoh Controller Laravel untuk menyimpan data laporan beserta titik koordinat
public function store(Request $request)
{
    $validated = $request->validate([
        'description' => 'required|string',
        'latitude' => 'required|numeric',
        'longitude' => 'required|numeric',
        'image_path' => 'nullable|image'
    ]);

    $report = Report::create([
        'description' => $validated['description'],
        // Menyimpan koordinat spasial
        'location' => DB::raw("ST_GeomFromText('POINT({$validated['longitude']} {$validated['latitude']})')"),
        'status' => 'pending'
    ]);

    return response()->json(['message' => 'Laporan spasial berhasil disimpan!', 'data' => $report]);
}